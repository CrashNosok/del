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
        public MainWindow()
        {
            InitializeComponent();
        }
        private void button_click(object sender, RoutedEventArgs e)
        {
            //MessageBox.Show(mask.Text.ToString());
            //MessageBox.Show(ip.Text.ToString());

            int my_mask;
            bool result;
            string[] nums = ip.Text.ToString().Split(new char[] { '.' });
            int num1;
            int num2;
            int num3;
            int num4;

            result = Int32.TryParse(mask.Text.ToString(), out my_mask);
            if (result)
            {
                Int32.TryParse(mask.Text.ToString(), out my_mask);
                Int32.TryParse(nums[0], out num1);
                Int32.TryParse(nums[1], out num2);
                Int32.TryParse(nums[2], out num3);
                Int32.TryParse(nums[3], out num4);

                MessageBox.Show(my_mask.ToString());
                MessageBox.Show(num1.ToString());
                MessageBox.Show(num2.ToString());
                MessageBox.Show(num3.ToString());
                MessageBox.Show(num4.ToString());


            }
            else
            {
                MessageBox.Show("Маска введена неправиьлно");
            }
        }
    }
}
