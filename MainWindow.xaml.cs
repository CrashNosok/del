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

namespace WpfApp2
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        string leftop = "";
        string operation = "";
        string rightop = "";
        public MainWindow()
        {
            InitializeComponent();
            //// создание виджетов через с#
            //Button myButton = new Button();
            //myButton.Width = 100;
            //myButton.Height = 30;
            //myButton.Content = "click me";
            //// += потому что на кнопке может быть не одно событие
            //myButton.Click += button_click;
            //myButton.Background = new System.Windows.Media.SolidColorBrush(System.Windows.Media.Colors.Red);
            //grid1.Children.Add(myButton);

            // добавить обработчикти для всех кнопок на гриде
            foreach (UIElement c in grid1.Children)
            {
                if (c is Button)
                {
                    ((Button)c).Click += button_click;
                }
            }

        }

        private void button_click(object sender, RoutedEventArgs e)
        {
            string s = (string)((Button)e.OriginalSource).Content;
            MessageBox.Show(s);
        }

        //private void button_click(object sender, RoutedEventArgs e)
        //{
        //    // получили текст из TextBox
        //    string text = textBox1.Text;
        //    if (text != "")
        //    {
        //        MessageBox.Show(text);
        //        // почистить TextBox
        //        textBox1.Text = "";
        //    }
        //}
    }
}
