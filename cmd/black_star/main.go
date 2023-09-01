package main

import (
	"fmt"
	"time"
)

func clear_screen() {
	fmt.Print("\033[H\033[2J")
}

func main() {
	clear_screen()

	intro := "In the future,\n"
	intro += "in a star system very far away...\n\n"
	fmt.Println(intro)
	time.Sleep(2 * time.Second)

	intro_2 := "Black Star\n"
	intro_2 += "A Text-Based Adventure\n"
	intro_2 += "Developed by Ryan Butler"
	fmt.Println(intro_2)
	time.Sleep(2 * time.Second)

	clear_screen()

	for {
		var user_input string

		menu := "Black Star\n"
		menu += "A Text-Based Adventure\n\n"
		menu += "MAIN MENU\n"
		menu += "1. Play\n"
		menu += "2. Quit"

		fmt.Println(menu)
		fmt.Println(">> ")

		fmt.Scan(&user_input)
		if user_input == "1" {
			fmt.Println("Game started...")
			time.Sleep(2 * time.Second)
			clear_screen()
			break
		} else {
			fmt.Println("Goodbye, see you again soon...")
			time.Sleep(2 * time.Second)
			clear_screen()
			break
		}
	}
}
