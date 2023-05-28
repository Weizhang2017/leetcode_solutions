//https://open.kattis.com/problems/abc
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
    "sort"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
    numbers, _ := reader.ReadString('\n')
    alphabets, _ := reader.ReadString('\n')
    m := make(map[string]int)
    var numbers_int []int
    numbers_ := strings.Fields(numbers)
    for _, v := range numbers_ {
    	i, _ := strconv.Atoi(v)
    	numbers_int = append(numbers_int, i)
    }
    sort.Ints(numbers_int)
    m["A"] = numbers_int[0]
    m["B"] = numbers_int[1]
    m["C"] = numbers_int[2]
    fmt.Printf("%v %v %v", m[string(alphabets[0])], m[string(alphabets[1])] ,m[string(alphabets[2])])
}