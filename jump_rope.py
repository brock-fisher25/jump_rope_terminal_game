from time import sleep
import time as ti

def main():
	countdown()

def flush_input():   
	try:
		import msvcrt
		while msvcrt.kbhit():
			msvcrt.getch()
	except ImportError:
		import sys, termios    #for linux/unix
		termios.tcflush(sys.stdin, termios.TCIOFLUSH)


def countdown():
	print("Get ready!")
	print("Countdown begins")
	for x in reversed(range(3)):
		print(x)
		sleep(1)
	print("Begin!")
	main_game()

def main_game():	
	successful_jump = True
	jumps = 0
	while successful_jump:
		sleep(0.2)
		frame_0()
		sleep(0.2)
		frame_1()
		sleep(0.2)
		frame_2()
		sleep(0.2)
		frame_3()
		sleep(0.2)
		frame_4()
		beg_time = ti.time()
		flush_input()
		received_input = input()
		if received_input == "":
			end_time = ti.time()
			final_time = (end_time - beg_time)
			if final_time < 0.3:
				jumps = jumps + 1
			else:
				successful_jump = False
	final_score(jumps)

def final_score(jumps):
	print("You were hit in the shins by the rope.\n"
	       "You successfully jumped " + str(jumps) + " ropes!.\n"
	       "To play again, restart the program.")
		
def frame_0():
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print("          \n"
		  "          \n"
	      "     O    \n"
	      "   _/|\_  \n"
	      "  |  |  | \n"
	      "  |_/_\_|")
def frame_1():
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print("          \n"
		  "          \n"
	      "     O    \n"
	      "   _/|\_  \n"
	      "  |__|__| \n"
	      "    / \  ")
def frame_2():
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print("          \n"
		  "          \n"
	      "   __O__  \n"
	      "  |_/|\_| \n"
	      "     |    \n"
	      "    / \  ")
def frame_3():
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print("   _____  \n"
	      "  /     \ \n"
	      "  |  O  | \n"
	      "  |_/|\_| \n"
	      "     |    \n"
	      "    / \  ")
def frame_4():
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print("          \n"
		  "          \n"
	      "     O    \n"
	      "   _/|\_  \n"
	      "  |  |  | \n"
	      "  | / \ | \n"
	      "  \_____/")
	
if __name__ == '__main__':
	main()