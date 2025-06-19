#include <iostream>
#include <windows.h>
#include <conio.h>
#include <thread>
#include <chrono>
#include <map>

using namespace std;

// Ноты и чистоты нот
map<char, pair<string, int>> keyToNote = {
    {'a', {"C", 262}}, {'s', {"D", 294}}, {'d', {"E", 330}}, {'f', {"F", 349}},
    {'g', {"G", 392}}, {'h', {"A", 440}}, {'j', {"B", 494}}, {'k', {"C5", 523}},
    {'w', {"C#", 277}}, {'e', {"D#", 311}}, {'t', {"F#", 370}}, {'y', {"G#", 415}},
    {'u', {"A#", 466}}
};

// Воспроизведение звука
void playSound(int frequency, int duration) {
    Beep(frequency, duration);
}

// Отоброжение клавы
void drawPiano(bool* pressedKeys) {
    system("cls");

    // Как их там белые?
    cout << "  [A]  [S]  [D]  [F]  [G]  [H]  [J]  [K]" << endl;
    for (int i = 0; i < 8; i++) {
        char key = "asdfghjk"[i];
        if (pressedKeys[key]) {
            cout << "  ### ";
        }
        else {
            cout << "  ___ ";
        }
    }
    cout << endl;

    // Негры
    cout << "[W][E]   [T][Y][U]   " << endl;
    for (int i = 0; i < 5; i++) {
        char key = "wetyu"[i];
        if (i == 2) cout << "      ";
        if (pressedKeys[key]) {
            cout << "## ";
        }
        else {
            cout << "|| ";
        }
    }
    cout << endl << endl;

    // Ноты
    cout << " C  D  E  F  G  A  B  C5" << endl;
    cout << "C# D#   F# G# A#" << endl << endl;
}

// Функция для нажатия клавиши
void handleKeyPress(char key, bool* pressedKeys) {
    if (keyToNote.find(key) != keyToNote.end()) {
        pressedKeys[key] = true;
        drawPiano(pressedKeys);

        // Воспроиведение звука в отдельном потоке
        thread soundThread(playSound, keyToNote[key].second, 200);
        soundThread.detach();

        // Задержка
        this_thread::sleep_for(chrono::milliseconds(200));
        pressedKeys[key] = false;
        drawPiano(pressedKeys);
    }
}

int main() {
    // Инициализация массива для отслеживания нажатых клавиш
    bool pressedKeys[256] = { false };

    cout << "Консольное фортепиано" << endl;
    cout << "Используйте клавиши A,S,D,F,G,H,J,K для белых клавиш" << endl;
    cout << "И W,E,T,Y,U для черных клавиш" << endl;
    cout << "Нажмите 'q' для выхода" << endl << endl;

    drawPiano(pressedKeys);

    while (true) {
        if (_kbhit()) {
            char key = tolower(_getch());

            if (key == 'q') {
                break;
            }
            else {
                handleKeyPress(key, pressedKeys);
            }
        }
    }

    return 0;
}