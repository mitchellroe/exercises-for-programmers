package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("What is the input string? ")
	myString, _ := reader.ReadString('\n')
	myString = strings.Replace(myString, "\n", "", -1)

	myCount := len(myString)

	output := myString + " has " + strconv.Itoa(myCount) + " characters."

	fmt.Println(output)

}
