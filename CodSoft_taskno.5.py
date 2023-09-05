from tkinter import *

question = {
	"1. What Indian city is the capital of two states?": ['Chandigarh', 'Kolkata', 'Delhi', 'Bangalore'],
	"2. Which city is the Capital of India?": ['Jaipur', 'Delhi', 'Chennai', 'Mumbai'],
	"3. Smallest State of India?": ['Rajasthan', 'Punjab', 'Goa', 'Bihar'],
        "4. Where is Taj Mahal Located?": ['Lucknow', 'Agra', 'Bhopa', 'Delhi'],
        "5. Who was the First President of India?": ['Dr B R Ambhedkar', 'Dr Rajendar Prasad', 'APJ Abdul Kalam', 'Dr Manmohan singh']
}

ans = ['Chandigarh', 'Delhi', 'Goa', 'Agra', 'Dr Rajendar Prasad']

current_question = 0


def start():
	start_button.forget()
	next_button.pack()
	nextquestion()


def nextquestion():
	global current_question
	if current_question < len(question):
		
		checkanswers()
		user_ans.set('None')
		c_question = list(question.keys())[current_question]
		
		clearframe()
		
		Label(f1, text=f"Question : {c_question}", padx=17, font="calibre 12 normal").pack(anchor=NW)
		
		for option in question[c_question]:
			Radiobutton(f1, text=option, variable=user_ans, value=option, padx=30).pack(anchor=NW)
		current_question += 1
	else:
		next_button.forget()
		checkanswers()
		clearframe()
		output = f"Your Score is {user_score.get()} out of {len(question)}"
		Label(f1, text=output, font="calibre 25 bold").pack()
		Label(f1, text="Thanks for Participating", font="calibre 18 bold").pack()
 
def checkanswers():
	temp_ans = user_ans.get()
	if temp_ans != 'None' and temp_ans == ans[current_question-1]:
		user_score.set(user_score.get()+1)


def clearframe():
	for widget in f1.winfo_children():
		widget.destroy()


if __name__ == "__main__":
	root = Tk()

	root.title("General Knowlege Quiz")
	root.geometry("960x630")
	root.minsize(900, 500)

	user_ans = StringVar()
	user_ans.set('None')
	user_score = IntVar()
	user_score.set(0)

	Label(root, text="GK Quiz", font="calibre 40 bold", relief=SUNKEN, background="green", foreground="blue", padx=10, pady=9).pack()
	
	Label(root, text="", font="calibre 10 bold").pack()
	start_button = Button(root, text="Start Quiz", command=start, font="calibre 17 bold")
	
	start_button.pack()

	f1 = Frame(root)
	f1.pack(side=TOP, fill=X)

	next_button = Button(root, text="Next Question", command=nextquestion, font="calibre 17 bold")

	root.mainloop()
