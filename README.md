# Определение координат круглых объектов в собственной системе координат

## Определение координат на готовом изображении 

С помощью скрипта image_processing можно определить координаты на имеющимся у вас изображении. Изображение необходимо поместить в папку 'imgs'.

1. При запуске скрипта, в терминале у вас запросит ввести имя файла с расширением (Имя_изображения.расширение файла).

![start_img](https://github.com/gitzense/caps_coordinates/assets/114235388/d55fad88-559c-4c25-b663-1880c8d33886)

2. После того, как ввели назвалие файла появится ваше изображение с выделенными окружностями и их координатами. Также координаты выводятся в терминале. Началом координат считается окружность, находящаяся ближе всего к левому нижнему углу изображения.

![work_img](https://github.com/gitzense/caps_coordinates/assets/114235388/520eaddc-3997-42b2-ad98-b49529b00543)

В случае, если на изображении обнаруживаются окружности, которых не было на изображении, можно это исправить меняя параметры слайдеров. Подгоняйте параметры, пока не избаветесь от артефактных окружностей на изображении. 

![sliders_img](https://github.com/gitzense/caps_coordinates/assets/114235388/7260afda-9409-455f-a8c5-5dc555c0e065)

3. Некоторые параметры могут вызвать ошибки, если в терминале появилось сообщение: 'Упс! Ошибочка вышла, не перебарщивайте с параметрами!', измените параметр, вывзвавший ошибку.

![error_img](https://github.com/gitzense/caps_coordinates/assets/114235388/8705841f-481a-49b6-8f05-cbdeaf5eb0ac)

4. Если необходимо сохранить получившиеся изображение нажмите клавишу 's' (раскладка должна быть английская). Изображение будет в папке imgs с названием 'circle_screen_{время сохранения}'.
  
5. Чтобы закрыть программу нажмите 'e' (английская раскладка) или ctrl+c в терминале.

## Определение координат с использованием камеры

С помощью скрипта video_processing можно определять координаты с изображений, сделанных с помощью подключенной подключенной к компьютеру камере. При запуске скрипта в папке 'imgs' создастся папка с названием '{дата_время}'. В папке будут сохраняться изображения сделанные с камеры. 

1. После запуска скрипта, включится камера. Расположите перед камерой, что необходимо.

![cap_video](https://github.com/gitzense/caps_coordinates/assets/114235388/c540117a-9cae-425e-a678-910ca0fba629)

2. Когда будет нужно определить координаты, нажмите клавишу 's' (английская раскладка). Появится новое окно, с настройками как в разделе 'Определение координат на готовом изображении'. Также в папке появится ваше изображение, которое вы будете обрабатывать с названием 'screen{номер скрина}'. Если, после определения координат, вам необходимо сохранить обработанное изображение нажмите 's' (ангийская раскладка). В папке появится изображнение с названием 'circle_screen{номер скрина}'.

![screen_video](https://github.com/gitzense/caps_coordinates/assets/114235388/134837a0-ae76-4d1e-ba49-9db3a0b937da)

3. Если нужно вернуться к камере для того, чтобы что-то изменить, нажмите клавижу 'c' (английская раскладка). Для обработки нового изображения повторить действия из пунтка 2.

4. Чтобы закрыть программу нажмите 'e' (английская раскладка) или ctrl+c в терминале.




