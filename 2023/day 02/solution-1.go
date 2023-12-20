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
	bag := Bag{"blue": 14, "red": 12, "green": 13}
	sum, err := calculateSum("input", bag)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(sum)
}

func calculateSum(filename string, bag Bag) (int, error) {
	file, err := os.Open(filename)
	if err != nil {
		return 0, err
	}
	defer file.Close()

	sum := 0
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		possible, id := isGamePossible(scanner.Text(), bag)
		if possible {
			sum += id
		}
	}

	if err := scanner.Err(); err != nil {
		return 0, err
	}

	return sum, nil
}

func isGamePossible(gameText string, bag Bag) (bool, int) {
	possible := true
	splitInput := strings.Split(gameText, ":")
	id, _ := strconv.Atoi(strings.Split(splitInput[0], " ")[1])
	curLine := splitInput[1]

	for _, draw := range strings.Split(curLine, ";") {
		for _, colour := range strings.Split(draw[1:], ", ") {
			colourMapping := strings.Split(colour, " ")
			n, _ := strconv.Atoi(colourMapping[0])
			possible = possible && (n <= bag[colourMapping[1]])
		}
	}

	return possible, id
}