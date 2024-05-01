import os
import tkinter as tk
import numpy as np
import ai
import transformers
from tkinter import scrolledtext


class ChatroomApp:
    bot = ai.ChatBot(name="dev")
    nlp = transformers.pipeline(
        "conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"

    def __init__(self, master):
        self.master = master
        master.title("AI Chatroom")
        self.chat_display = scrolledtext.ScrolledText(
            master, state='disabled', wrap='word')
        self.chat_display.pack(expand=True, fill='both')

        # Create the message entry field
        self.entry_field = tk.Entry(master)
        self.entry_field.pack(fill='x')
        self.entry_field.bind("<Return>", self.send_message)
        self.send_button = tk.Button(
            master, text="Send", command=self.send_message)
        self.send_button.pack()
        self.messages = []

    def process_message(self, message):
        if "time" in message:
            res = self.bot.action_time()
        elif any(i in message for i in ["thank", "thanks"]):
            res = "Assistant: "+np.random.choice(["you're welcome!", "anytime!", "no problem!",
                                                  "cool!", "I'm here if you need me!", "mention not"])
        else:
            if self.bot.text == "ERROR":
                res = "Assistant: Sorry, come again?"
            else:
                chat = self.nlp(transformers.Conversation(
                    message), pad_token_id=50256)
                res = str(chat)
                res = res[res.find("assistant:"):].strip()
        return res

    def ai_reply(self, message):
        res = self.process_message(message)
        self.messages.append(res)
        self.display_messages()
        self.entry_field.config(state='normal')

    def send_message(self, event=None):
        message = self.entry_field.get()
        if message.strip() != "":
            self.messages.append("You: " + message)
            self.display_messages()
            self.entry_field.delete(0, 'end')
            self.chat_display.config(state='disabled')
            self.master.after(1000, self.ai_reply, message)

    def display_messages(self):
        self.chat_display.config(state='normal')
        self.chat_display.delete('1.0', 'end')
        for msg in self.messages:
            self.chat_display.insert('end', msg + '\n')
        self.chat_display.see('end')
        self.chat_display.config(state='disabled')


def main():
    root = tk.Tk()
    app = ChatroomApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
