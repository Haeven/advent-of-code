class Solution extends AbstractDay
{
    /** @var array<string, array{type: string, destinations: string[]}> */
    private array $modules = [];

    public function parseInput(): void
    {
        $this->modules = [];

        foreach ($this->getInputAsArray() as $row) {
            preg_match('/([%&]?)(\w+) -> (.+)/', $row, $matches);
            $this->modules[$matches[2]] = ['type' => $matches[1], 'destinations' => explode(', ', $matches[3])];
        }
    }

    public function part1(): string|int
    {
        $state = [];

        foreach ($this->modules as $moduleName => $module) {
            if ('%' == $module['type']) {
                $state[$moduleName] = false;
            }

            foreach ($module['destinations'] as $destination) {
                if ('&' == ($this->modules[$destination]['type'] ?? null)) {
                    $state[$destination][$moduleName] = 0;
                }
            }
        }

        $pulses = [0, 0];

        for ($i = 0; $i < 1000; ++$i) {
            $queue = [['broadcaster', 0, 'button']];

            while (!empty($queue)) {
                [$module, $pulse, $input] = array_shift($queue);
                ++$pulses[$pulse];
                $nextPulse = null;

                if (!isset($this->modules[$module])) {
                    continue;
                }

                if ('%' == $this->modules[$module]['type']) {
                    if (0 == $pulse) {
                        $nextPulse = $state[$module] ? 0 : 1;
                        $state[$module] = !$state[$module];
                    } else {
                        continue;
                    }
                } elseif ('&' == $this->modules[$module]['type']) {
                    $state[$module][$input] = $pulse;
                    $nextPulse = 0;

                    foreach ($state[$module] as $v) {
                        if (1 != $v) {
                            $nextPulse = 1;
                            break;
                        }
                    }
                } elseif ('broadcaster' == $module) {
                    $nextPulse = $pulse;
                }

                foreach ($this->modules[$module]['destinations'] as $destination) {
                    $queue[] = [$destination, $nextPulse, $module];
                }
            }
        }

        return array_product($pulses);
    }

    public function part2(): string|int
    {
        $state = [];
        $rxInput = null;

        foreach ($this->modules as $moduleName => $module) {
            if ('%' == $module['type']) {
                $state[$moduleName] = false;
            }

            foreach ($module['destinations'] as $destination) {
                if ('&' == ($this->modules[$destination]['type'] ?? null)) {
                    $state[$destination][$moduleName] = 0;
                }

                if ('rx' == $destination) {
                    $rxInput = $moduleName;
                }
            }
        }

        $press = 0;
        $rxInputInputsFrequencies = [];

        while (count($rxInputInputsFrequencies) < count($state[$rxInput])) {
            ++$press;
            $queue = [['broadcaster', 0, 'button']];

            while (!empty($queue)) {
                [$module, $pulse, $input] = array_shift($queue);
                $nextPulse = null;

                if ($module == $rxInput && 1 == $pulse) {
                    $rxInputInputsFrequencies[$input] ??= $press;
                }

                if (!isset($this->modules[$module])) {
                    continue;
                }

                if ('%' == $this->modules[$module]['type']) {
                    if (0 == $pulse) {
                        $nextPulse = $state[$module] ? 0 : 1;
                        $state[$module] = !$state[$module];
                    } else {
                        continue;
                    }
                } elseif ('&' == $this->modules[$module]['type']) {
                    $state[$module][$input] = $pulse;
                    $nextPulse = 0;

                    foreach ($state[$module] as $v) {
                        if (1 != $v) {
                            $nextPulse = 1;
                            break;
                        }
                    }
                } elseif ('broadcaster' == $module) {
                    $nextPulse = $pulse;
                }

                foreach ($this->modules[$module]['destinations'] as $destination) {
                    $queue[] = [$destination, $nextPulse, $module];
                }
            }
        }

        return array_reduce($rxInputInputsFrequencies, 'gmp_lcm', 1);
    }
}