import time

import pyperclip

QA_DATABASE = {
    "Аппаратный или программный элемент, который позволяет устройству (например, компьютеру) подключаться к сети и обмениваться данными с другими устройствами, называют": "Интерфейсом",
    "Показатель, который выражает отношение мощности полезного сигнала к мощности нежелательного шума.": "соотношение сигнал/шум",
    "Коммуникационный протокол описывающий формат пакета данных называется:": "TCP/IP",
}


class ClipboardWatcher:
    def __init__(self, initial_value=""):
        self.recent_value = initial_value

    def find_answer(self, question_text):
        clean_question = " ".join(question_text.strip().split()).lower()

        if not clean_question:
            return None

        for q, a in QA_DATABASE.items():
            clean_q_from_db = " ".join(q.strip().split()).lower()
            if clean_question in clean_q_from_db or clean_q_from_db in clean_question:
                return a
        return None

    def run(self):
        while True:
            clipboard_content = pyperclip.paste()

            if clipboard_content and clipboard_content != self.recent_value:
                self.recent_value = clipboard_content
                answer = self.find_answer(clipboard_content)

                if answer:
                    pyperclip.copy(answer)
                    self.recent_value = answer

            time.sleep(0.8)


if __name__ == "__main__":
    startup_message = "))"
    pyperclip.copy(startup_message)
    watcher = ClipboardWatcher(initial_value=startup_message)
    watcher.run()
