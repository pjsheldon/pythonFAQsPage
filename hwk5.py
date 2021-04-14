'''--------By: PJ Sheldon---------
	--------Date: 8/8/20---------
	hwk5.py programming assignment 5
	SEC-290 Wilmington University'''

	# Menu 1 thru 4 for the while loop
menu = """
0: Exit
1: List FAQ's 
2: Add FAQ's
3: Delte FAQ's
"""

# THE FAQ's Dictionary
faqs = {}


done = False                            # Exit variable as False

while not done:
	print("==========================") # program title
	print("FREQUENTLY ASKED QUESTIONS")
	print("==========================")
	print()                             # spacing
	print(menu)
	selection = input("please make a selection between 0 and 3: ") # input for menu
	print()

	if selection == "0":                # the exit selection
		done = True # variable is oppistie of while loop statement making the while loop false and claosing it
		print('Good bye!')
		print('Thanks for Playing!')    # Exit messaging.

	elif selection == "1":              # List FAQ's
		print("LIST THE FAQ'S IN NOTEBOOK") # selection title
		print()

		keys = faqs.keys() # syntax for the keys

		for key in keys:                # for loop that pulls the list of the keys 
			print('Question: {}'.format(key)) # Keys in disctionary
			print('Answer: {}'.format(faqs[key])) # values in dictionary
			print()


	elif selection == "2":
		print()
		print("ADD FAQ'S") # selection title 
		print()
		while True:                        # While statement for question validation
			key = input('Please enter the question: ') # key input question 
		
			if key not in faqs:
				value = input('Please enter the answer: ') # value iput question
				print()
				faqs[key] = value           # adds to dictionary

		
				print("{}: {}".format(key, value)) # to show question and answer from the input
				print()
				print()
				print('This has been added to the FAQs notebook.') # this is to affirm added to dictionary 
				print()
				break                                            # if the answer is complete the while loop is done
			else:                                                # keep the question going if was not the right answer the first time
				print()
				print("{} has already been used in the FAQs notebook.\nCan you please rephase the question?".format(key)) # wrong answer result
				print()
				
	elif selection == "3":
		while True:                                      # while loop for deleting question 
			delete = input('Please enter a question to be deleted: ')

			if delete in faqs:                           # if the question to delete is correct then the question is deleted 
				del(faqs[delete])
				print()
				print('{} was deleted from FAQs notebook'.format(delete)) # result statement
				print()
				print()
				print('Notebook updated')               # update statement 
				print()
				break                                   # breaks the loop
			else:
				print()
				print('Could not find {} in FAQs Notebook.'.format(delete)) # when the question is not in dictionary it will resule and ask again
				print('FAQs notebook was not updated')
				print()

	else:
		print("please select 0, 1, 2, or 3") # if the wrong menu number is entered
		print()