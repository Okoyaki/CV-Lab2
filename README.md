# CV Лабораторная работа №2
## Цель работы
Реализовать простейшие алгоритмы сопоставления изображений
## Задание
1. Реализовать программу согласно описанию. Можно использовать языки C++ или Python и любые библиотеки.
2. Сравнить качество работы двух вариантов реализации по точности детектирования.
3. Сделать отчёт в виде readme на GitHub,там же должен быть выложен исходный код.
## Теоретическая база
<b>Template Matching</b> (шаблонное сопоставление) — это метод из области компьютерного зрения, который применяется для поиска и определения положения заданного образца (шаблона) на изображении. Этот подход прост и эффективен, особенно в случаях, когда размер, ориентация и освещённость объекта остаются неизменными.

Template Matching сравнивает небольшой участок изображения (шаблон) с различными частями большего изображения и определяет, насколько они похожи. Это достигается с помощью методов корреляции или оценки степени совпадения.

<b>Алгоритм SIFT</b> (Scale-Invariant Feature Transform) выявляет ключевые точки на изображении, устойчивые к изменениям масштаба, поворота и частично освещения. Он строит масштабное пространство, используя размытие Гаусса, и ищет экстремумы в разностях между уровнями. Отфильтровав точки с низким контрастом и на краях, для каждой ключевой точки определяет ориентацию на основе локальных градиентов. Далее создаётся дескриптор — вектор, описывающий окрестности точки. Этот дескриптор позволяет эффективно сопоставлять точки между изображениями, обеспечивая надёжное распознавание объектов.

## Описание разработанной системы
Для реализации функции сопоставления шаблона была использована функция ```cv2.matchTemplate``` из библиотеки OpenCV.

Для реализации алгоритма SIFT был использован набор функций по поиску и сопоставлению ключевых точек из OpenCV.

Ниже приведен пример исходных изображений и эталоны, использованные при поиске:

![alt text](https://github.com/Okoyaki/CV-Lab2/blob/24a52a2084a045c0af6055c0f15c0bcb113fd38d/data/orig/images/img1.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/24a52a2084a045c0af6055c0f15c0bcb113fd38d/data/orig/templates/img1.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/24a52a2084a045c0af6055c0f15c0bcb113fd38d/data/orig/templates_add/img1.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/24a52a2084a045c0af6055c0f15c0bcb113fd38d/data/orig/images/img2.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/24a52a2084a045c0af6055c0f15c0bcb113fd38d/data/orig/templates/img2.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/24a52a2084a045c0af6055c0f15c0bcb113fd38d/data/orig/templates_add/img2.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/24a52a2084a045c0af6055c0f15c0bcb113fd38d/data/orig/images/img3.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/24a52a2084a045c0af6055c0f15c0bcb113fd38d/data/orig/templates/img3.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/24a52a2084a045c0af6055c0f15c0bcb113fd38d/data/orig/templates_add/img3.jpg)

## Результаты работы и тестирования системы
В результате выполнения алгоритмов были получены изображения с обозначенными в рамках обнаруженные эталонные объекты:

### 1. Сопоставление шаблонов
Первый шаблон:
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/eb5e409a981cf60fe3654e5671f92c4b0ced2e64/data/result/tm/temp/img0.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/eb5e409a981cf60fe3654e5671f92c4b0ced2e64/data/result/tm/temp/img1.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/eb5e409a981cf60fe3654e5671f92c4b0ced2e64/data/result/tm/temp/img2.jpg)

Второй шаблон:
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/841a59ab438bebf4ffe23363d3e0c2008a6648f3/data/result/tm/temp_add/img0.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/841a59ab438bebf4ffe23363d3e0c2008a6648f3/data/result/tm/temp_add/img1.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/841a59ab438bebf4ffe23363d3e0c2008a6648f3/data/result/tm/temp_add/img2.jpg)

### 2. Алгоритм SIFT
Первый шаблон:

![alt text](https://github.com/Okoyaki/CV-Lab2/blob/eb5e409a981cf60fe3654e5671f92c4b0ced2e64/data/result/kp/temp/img0.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/eb5e409a981cf60fe3654e5671f92c4b0ced2e64/data/result/kp/temp/img1.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/eb5e409a981cf60fe3654e5671f92c4b0ced2e64/data/result/kp/temp/img2.jpg)

Второй шаблон:
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/e72bb86337304a281ef152cf995fe143d0fa9bce/data/result/kp/temp_add/img0.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/e72bb86337304a281ef152cf995fe143d0fa9bce/data/result/kp/temp_add/img1.jpg)
![alt text](https://github.com/Okoyaki/CV-Lab2/blob/e72bb86337304a281ef152cf995fe143d0fa9bce/data/result/kp/temp_add/img2.jpg)

## Выводы по работе

В результате выполнения работы оба алгоритма успешно справились с поставленной задачей: были успешно найдены оба вида эталонов для каждого изображения