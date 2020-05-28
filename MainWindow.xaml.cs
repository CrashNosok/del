using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfApp10
{
    public partial class MainWindow : Window
    {
        public bool check_mask(string mask_b)
        {
            bool sign;

            // знак, который показывает, правильно ли введена маска
            sign = true;
            // внешним циклом ищем нули
            for (int i = 0; i < mask_b.Length; i++)
            {
                if (mask_b[i] == '0')
                {
                    // ищем 1
                    for (; i < mask_b.Length; i++)
                    {
                        // если нашли 1, значит маска введена неправильно
                        if (mask_b[i] == '1')
                            sign = false;
                    }
                }
            }
            return sign;
        }

        public int count_zero(string number_str)
        {
            // счётчик цикла
            int i;
            // кол-во нулей
            int count;

            i = 0;
            count = 0;
            // проверка, если число обрезалось
            if (number_str.Length < 8)
            {
                // заполняем недостающими нулями
                for (int j = 0; number_str.Length < 8; j++)
                    number_str += "0";
            }
            // считаем нули
            while (i < number_str.Length)
            {
                if (number_str[i] == '0')
                    count++;
                i++;
            }
            return (count);
        }

        public MainWindow()
        {
            InitializeComponent();
        }

        private void button_click(object sender, RoutedEventArgs e)
        {
            // кол-во октетов
            const int size = 4;
            // кол-во нулей в маске
            int n = 0;
            // массив чисел из ip адреса
            string[] nums = ip.Text.ToString().Split(new char[] { '.' });
            // массив чисел из маски
            string[] my_mask = mask.Text.ToString().Split(new char[] { '.' });
            // строка с адресом подсети
            string subnet = "";
            // массив из 4 чисел для хранения октетов ip адреса
            int[] ip_arr = new int[size];
            // массив из 4 чисел для хранения октетов маски
            int[] mask_arr = new int[size];
            // переменная для хранения маски в 2-ом виде
            string mask_binary = "";
            // переменная для проверки
            bool check;

            if (nums.Length == 4 && my_mask.Length == 4)
            {
                for (int i = 0; i < size; i++)
                {
                    // заполняем массив ip адресов
                    check = Int32.TryParse(nums[i], out ip_arr[i]);
                    // проверка, получилось ли спрарсить число
                    if (check == false)
                    {
                        MessageBox.Show("ip-адрес введён неправильно");
                        break;
                    }
                    // заполняем массив маски
                    check = Int32.TryParse(my_mask[i], out mask_arr[i]);
                    // проверка, получилось ли спрарсить число
                    if (check == false)
                    {
                        MessageBox.Show("Маска введёна неправильно");
                        break;
                    }
                }

                // создаём маску в бинарном виде
                for (int i = 0; i < size; i++)
                {
                    mask_binary += Convert.ToString(mask_arr[i], 2);
                }
                // проверяем, что маска корректна (после единиц идут только нули)
                if (check_mask(mask_binary) == false)
                    MessageBox.Show("Маска введёна неправильно");
                else
                {
                    for (int i = 0; i < size; i++)
                    {
                        // считаем кол-во нулей в октете в маске (отправляем число в 2-ом виде в функцию,
                        // которая считает кол-во нулей)
                        n += count_zero(Convert.ToString(mask_arr[i], 2));
                        // заполняем адрес подсети
                        subnet += (ip_arr[i] & mask_arr[i]).ToString();
                        // делаем, чтобы последняя точка в адресе подсети не ставилась
                        if (i < size - 1)
                            subnet += ".";
                    }
                    // выводим вдрес подсети
                    MessageBox.Show(subnet);
                    // выводмим кол-во возможных хостов в сети (не считая широковещательный адрес)
                    MessageBox.Show((Math.Pow(2, n) - 2).ToString());
                }
            }
            else
            {
                MessageBox.Show("Маска или ip-адрес введён неправильно");
            }
        }
    }
}
