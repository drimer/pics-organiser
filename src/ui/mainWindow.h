#ifndef __MAIN_WINDOW
#define __MAIN_WINDOW

#include "ui_mainWindow.h"
#include <QSpinBox>
#include <QAction>

class MainWindow : public QMainWindow{
Q_OBJECT

  private:
  Ui::VentanaPrincipal ui;
  
  void creaInterfaz();

 public:
  MainWindow(QWidget *parent = 0);

};

#endif /*__MAIN_WINDOW*/
