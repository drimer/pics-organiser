#include <iostream>

#include <QApplication>

#include "ui/mainWindow.h"

using namespace std;


int main(int argc, char **argv){

#if defined(QT)
  QApplication app(argc, argv);
  
  QWidget *win = new MainWindow();
  win->show();
  
  return app.exec();
#else
  cout << "Using WINX" << endl;
#endif

  return 0;
}
