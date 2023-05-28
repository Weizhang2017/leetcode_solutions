// https://open.kattis.com/problems/bluetooth

package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
    "time"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
    n_, _ := reader.ReadString('\n')
    start := time.Now()
    n, err := strconv.Atoi(strings.TrimSpace(n_))
    if err != nil {
        fmt.Println(err)
        os.Exit(2)
    }
    teeth := [][]int{[]int{0, 0}, []int{0, 0}}
    blue := []int{0, 0}
    for i := 0; i < n; i++ {
    	tooth, _ := reader.ReadString('\n')
    	tooth_ := strings.Fields(strings.TrimSpace(tooth))
    	if strings.Contains("+-", tooth_[0][:1]) {
    		if tooth_[1] == "b" {
    			blue[0] = 1
    		}
    		if "+" == tooth_[0][:1] {
    			teeth[0][0] += 1
    		} else {
    			teeth[0][1] += 1
    		}
    		
    	} else {
    		if tooth_[1] == "b" {
    			blue[1] = 1
    		}
    		if "+" == tooth_[0][1:2] {
    			teeth[1][0] += 1
    		} else {
    			teeth[1][1] += 1
    		}
    	}
    }
    
    if blue[0] == 1 && blue[1] == 1 {
    	fmt.Println(2)
    } else {
    	if teeth[0][0] < 8 && teeth[0][1] < 8 && blue[0] != 1 {
    		fmt.Println(0)
    	} else if teeth[1][0] < 8 && teeth[1][1] < 8 && blue[1] != 1 {
    		fmt.Println(1)
    	} else {
    		fmt.Println(2)
    	}
    }
    fmt.Println(time.Since(start))
}
