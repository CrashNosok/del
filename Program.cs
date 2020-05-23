using System;

namespace ConsoleApp11
{

    //написать свой собственный класс Exception
    //добавить пару полей для более конкртетной информации(public)
    // добавить пару методов(public)
    // try/catch/catch/catch/catch/catch/finaly

    class MyOwnException : Exception
    {
        public MyOwnException() : base("Это моё исключение!!")
        {
        }

        public MyOwnException(string message) : base(message)
        {
        }
    }


    class Program
    {
        static void Main(string[] args)
        {
            // исключения. синтаксис
            int i = 1;
            try
            {
                //int i = 5;
                //int j = i / 9;
                //Console.WriteLine(j);

                //int a = 2000000000;
                //int b = 2000000000;
                //int c = checked(a * b);
                //Console.WriteLine(c);

                //Exception ex = new Exception();
                //throw new MyOwnException();
                throw new ArgumentNullException("i", "qqq");

            }
            catch (MyOwnException ex)
            {
                Console.WriteLine(ex.Message);
            }
            catch (DivideByZeroException ex) when (i == 5)
            {
                Console.WriteLine($"1) i = {i}");
                Console.WriteLine(ex.Message);
            }
            catch (DivideByZeroException ex)
            {
                Console.WriteLine($"2) i = {i}");
                Console.WriteLine(ex.Message);
            }
            catch (OverflowException ex)
            {
                Console.WriteLine(ex.Message);
            }
            catch (Exception ex)
            {
                Console.WriteLine("работа завершена");
                Console.WriteLine(ex.Message);
                
            }
            finally
            {
                Console.WriteLine("Работает finaly");
            }


            //Console.WriteLine("Hello World!");
        }
    }
}
