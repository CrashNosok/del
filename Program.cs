using System;

namespace ConsoleApp3
{
    class Program
    {
        static void Main(string[] args)
        {
            //if - else if - else
            /*
            синтаксис:

            if (<условие 1>)
            {
                <блок действий 1 >;
            }
            else if (<условие 2>)
            {
                <блок действий 2>;
            }
            else if (<условие 3>)
            {
                <блок действий 3>;
            }
            else if (<условие 4>)
            {
                <блок действий 4>;
            }
            else
            {
                <блок действий 5>;
            }

            else if - необязательный блок, который позволяет 
                проверить дополнительное условие.
                находится между if и else

            */

            //int b = int.Parse(Console.ReadLine());
            //if (b > 0)
            //{
            //    int a = b % 5;
            //    if (a == 1)
            //    {
            //        Console.WriteLine("big");
            //    }
            //    else if (a == 2)
            //    {
            //        Console.WriteLine("point");
            //    }
            //    else if (a == 3)
            //    {
            //        Console.WriteLine("middle");
            //    }
            //    else if (a == 4)
            //    {
            //        Console.WriteLine("no name");
            //    }
            //    else if (a == 0)
            //    {
            //        Console.WriteLine("smallest");
            //    }
            //    else
            //    {
            //        Console.WriteLine("Error");
            //    }
            //}
            //else
            //{
            //    Console.WriteLine("Error");
            //}


            // пользователь вводит число.
            // вывести название пальца, который соответствует этому 
            // числу
            // 1 - большой
            // 2 - указат
            // 3 - средний
            // 4 - безымян
            // 5 - мизинец

            // 6 - большой
            // 7 - указат
            // 8 - средний
            // 9 - безымян
            // 10 - мизинец

            // 11 - большой
            // 12 - указат
            // 13 - средний
            // 14 - безымян
            // 15 - мизинец
            // ...
            // обработать все случаи

            /*
               a % 2    0, 1
               a % 3    0, 1, 2
               a % 4    0, 1, 2, 3
               a % 5    0, 1, 2, 3, 4
               ...      ...

                1 % 2 = 1
                если делимое меньше делителя при делении с остатком
                ответ всегда равен делимому
            */

            // switch
            //int a = int.Parse(Console.ReadLine());
            //switch (a)
            //{
            //    case 1: // если число а равно 1 (if a == 1)
            //        Console.WriteLine("единица");
            //        break;
            //    case 2: // (if a == 2)
            //        Console.WriteLine("двойка");
            //        break;
            //    case 3:
            //    case 4:
            //    case 5:
            //        Console.WriteLine("тройка");
            //        break;
            //    default: // как else
            //        Console.WriteLine("Неизвестное число");
            //        break;
            //  }

            // пользователь вводит свою оценку
            // если это 5, выводим отлично
            // если это 4, выводим хорошо
            // если это 3, выводим подучись
            // если это 2, выводим бездельник
            // в любом другом случае "error"


            int num = int.Parse(Console.ReadLine());
            if (num > 99 && num < 1000)
            {
                int a1;
                int a2;
                int a3;

                a3 = num % 10; // num = 123
                num = num / 10; // num = 12

                a2 = num % 10;
                num = num / 10; // num = 1

                a1 = num;
                if (a1 == a2 || a1 == a3 || a2 == a3)
                {
                    Console.WriteLine("есть одинаковые цифры");
                }
                else
                {
                    Console.WriteLine("нет одинаковых цифр");
                }
            }
            else
            {
                Console.WriteLine("Error");
            }
        }
    }
}
