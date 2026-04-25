import json

with open('notes.json', 'r', encoding='utf-8') as f:
    notes = json.load(f)

def add_note(notes):
    user_data = input('Enter a data: ')
    user_note = input('Enter a note: ')
    month = user_data[3:5]
    note = {user_data: user_note}
    if month not in notes:
        notes[month] = []
    notes[month].append(note)
    with open('notes.json', 'w', encoding='utf-8') as f:
        json.dump(notes, f, indent=4)
    return 'Note is already added!'

def find_note(notes):
    user_data = input('Enter a data ')
    for data in notes:
        for datas in notes[data]:
            if user_data in datas:
                return datas[user_data]
    return 'Note is missing!'

def view_notes(notes):
    user_month = input('Enter a month which notes you want to view: ')
    if user_month not in notes:
        return 'Notes of that month are missing!'
    else:
        return notes[user_month]

def statistics(notes):
    user_month = input('Enter a month which statistic you want to view: ')
    if user_month not in notes:
        return 'Notes of that month are missing!'
    count = len(notes[user_month])   
    return f'Count of notes during that month: {count}'

while True:
    print('1)Add a note\n2)Find a note\n3)View all notes\n4)View statistics')
    print('Check a variant!')
    user_answer = input('Enter an answer by number or (stop): ').lower()
    if user_answer == 'stop':
        break
    if int(user_answer) == 1:
        print(add_note(notes))
    elif int(user_answer) == 2:
        print(find_note(notes))
    elif int(user_answer) == 3:
        print(view_notes(notes))
    elif int(user_answer) == 4:
        print(statistics(notes))