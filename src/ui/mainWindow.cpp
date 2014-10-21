#include "mainWindow.h"
#include <QMenu>
#include <QFile>
#include <QMessageBox>
#include <QString>
#include <cstdlib>
using namespace std;

MainWindow::MainWindow(QWidget *parent)
  : QMainWindow(parent){
  creaInterfaz();  
}

void MainWindow::creaInterfaz(){
  ui.setupUi(this);
}
