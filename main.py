import os

class Phonebook:
    def __init__(self, filename):
        self.filename = filename
        self.entries = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    entry = line.strip().split(';')
                    self.entries.append(entry)

    def save_data(self):
        with open(self.filename, 'w') as file:
            for entry in self.entries:
                file.write(';'.join(entry) + '\n')

    def add_entry(self, data):
        self.entries.append(data)
        self.save_data()

    def edit_entry(self, index, data):
        if 0 <= index < len(self.entries):
            self.entries[index] = data
            self.save_data()

    def search_entries(self, search_terms):
        results = []
        for entry in self.entries:
            if all(term.lower() in entry_str.lower() for term, entry_str in zip(search_terms, entry)):
                results.append(entry)
        return results

def main():
    phonebook = Phonebook('phone_book.txt')

    while True:
        print("1. Вывести записи")
        print("2. Добавить новую запись")
        print("3. Редактировать запись")
        print("4. Поиск записей")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            page = 1
            entries_per_page = 10
            while True:
                start_idx = (page - 1) * entries_per_page
                end_idx = start_idx + entries_per_page
                for idx, entry in enumerate(phonebook.entries[start_idx:end_idx], start=start_idx + 1):
                    print(f"{idx}. {' | '.join(entry)}")
                    print("\nСтраница:", page)
                    print("N. Следующая страница")
                    print("P. Предыдущая страница")
                    print("B. Назад")
                choice = input("Выберите действие: ").upper()
                if choice == 'N':
                    page += 1
                elif choice == 'P':
                    page -= 1 if page > 1 else 0
                elif choice == 'B':
                    break

        elif choice == '2':
            data = input("Введите данные (через точку с запятой): ").split(';')
            phonebook.add_entry(data)

        elif choice == '3':
            index = int(input("Введите номер записи для редактирования: ")) - 1
            if 0 <= index < len(phonebook.entries):
                new_data = input("Введите новые данные (через знак ';'): ").split(';')
                phonebook.edit_entry(index, new_data)
                print("Запись успешно отредактирована.")

        elif choice == '4':
            search_terms = input("Введите характеристики для поиска (через знак ';'): ").split(';')
            results = phonebook.search_entries(search_terms)
            if results:
                for idx, entry in enumerate(results, start=1):
                    print(f"{idx}. {' | '.join(entry)}")
            else:
                print("Записи не найдены.")

        elif choice == '5':
            break


if __name__ == "__main__":
    main()