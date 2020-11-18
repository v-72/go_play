package main

import (
	"fmt"
	"sort"
	"strings"
)

func main() {
	arr := []string{"eat", "tea", "aet", "top", "pot", "treat"}
	anaMap := make(map[string][]string)
	for i := 0; i < len(arr); i++ {
		key := sortKey(arr[i])
		anaMap[key] = append(anaMap[key], arr[i])
		fmt.Println(anaMap)
	}
}

func sortKey(_str string) string {
	characters := strings.Split(_str, "")
	sort.Strings(characters)
	sortedStr := strings.Join(characters, "")
	return sortedStr
}
