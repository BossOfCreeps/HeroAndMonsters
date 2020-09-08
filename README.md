## Герой и чудовища

### Задание

Написать текстовую игру «герой и чудовища». 
Игрок - рыцарь в фантастической стране. Ваша задача - победить 10 чудовищ чтобы спасти королевство от нападения и тем самым выиграть игру.

#### Дано:
- Игра происходит по «ходам». Программа выводит на экран текст о том что происходит. Например :«Вы встретили чудовище с 4 жизнями и с силой удара 5»
- Управление событиями игры происходит с помощью ввода с клавиатуры цифр, либо «1», либо «2». Например, программа выводит на экран «1-атаковать чудовище, 2-убежать» и приглашение к вводу либо числа 1 либо 2. При вводе любого другого текста должно быть показано сообщение о некорректном вводе и приглашение на ввод «1» либо «2» должно быть показано заново, пока пользователь не введёт «1» либо «2».
- У рыцаря изначально 10 жизней и сила удара равна 10.
- Перед рыцарем случайно возникает либо очередное чудовище, либо увеличивающее случайное число здоровья яблочко, либо совершенно новый меч со случайной силой атаки.
- У чудовища есть случайное число здоровья и атаки, а у игрока - выбор (вводимый с клавиатуры) 1-сражаться, 2-убежать, чтобы набраться сил.
- В случае сражения рыцарь побеждает, если число его атаки превосходит число жизней чудовища. При этом чудовище отнимает у рыцаря число жизней, соответствующее его атаке.
- Если чудовище сильнее рыцаря, то есть если сила атаки чудовища превосходит количество жизней рыцаря — рыцарь умирает, выводится сообщение «игра окончена» и происходит завершение программы.
- При победе над 10 чудовищами, выводится сообщение «Победа!» и происходит завершение программы.
- При обнаружении меча, на экран должна быть выведена его сила атаки и игроку даётся (вводимый с клавиатуры) выбор 1-взять меч себе выбросив старый, 2-пройти мимо меча. При взятии нового меча сила атаки рыцаря принимается равной силе атаки нового подобранного меча.
- При обнаружении яблочка — рыцарь съедает его и узнаёт насколько он увеличил количество жизней и чему теперь равно его количество жизней. В случае нахождения яблочка игроку не даётся выбора действия.
- Границы случайных величин (кол-ва жизней чудовищ, силы их атаки, силы атаки мечей и количество жизней которое даёт яблочко) предлагается определить самостоятельно в границах от 5 до 30.

#### Требуется
- Написать текстовую игру по требованиям описанным выше.
- Использовать циклы при написании программы
- Использовать классы при написании программы
- Не использовать сторонние библиотеки

