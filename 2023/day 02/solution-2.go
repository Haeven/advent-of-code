package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Bag map[string]int

func main() {
	sum, err := calculateSum("input")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(sum)
}

func calculateSum(filename string) (int, error) {
	file, err := os.Open(filename)
	if err != nil {
		return 0, err
	}
	defer file.Close()

	sum := 0
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		bag := initializeBag()
		curLine := getGameText(scanner.Text())
		updateBag(bag, curLine)
		sum += calculateProduct(bag)
	}

	if err := scanner.Err(); err != nil {
		return 0, err
	}

	return sum, nil
}

func initializeBag() Bag {
	return Bag{"blue": 0, "red": 0, "green": 0}
}

func getGameText(line string) string {
	splitInput := strings.Split(line, ":")
	return splitInput[1]
}

func updateBag(bag Bag, line string) {
	for _, draw := range strings.Split(line, ";") {
		for _, colour := range strings.Split(draw[1:], ", ") {
			splitStr := strings.Split(colour, " ")
			n, _ := strconv.Atoi(splitStr[0])
			col := splitStr[1]
			if bag[col] < n {
				bag[col] = n
			}
		}
	}
}

func calculateProduct(bag Bag) int {
	return bag["blue"] * bag["red"] * bag["green"]
}
