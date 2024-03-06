# style components
button_style = """
            QPushButton {
                border-radius: 5px; /* Ajusta el valor para cambiar el radio del borde */
                background-color: darkblue; /* Color de fondo */
                color: white; /* Color del texto */
                font-size: 15px; /* Tamaño de la fuente */
                padding: 10px 10px; /* Espaciado interno */
            }

            QPushButton:hover {
                background-color: deep sky blue; /* Cambia el color de fondo al pasar el mouse */
            }
        """

button_sleep = """
            QPushButton {
                border-radius: 5px; /* Ajusta el valor para cambiar el radio del borde */
                background-color: tomato ; /* Color de fondo */
                color: white; /* Color del texto */
                font-size: 15px; /* Tamaño de la fuente */
                padding: 10px 10px; /* Espaciado interno */
            }

            QPushButton:hover {
                background-color: brown; /* Cambia el color de fondo al pasar el mouse */
            }
        """


progressBarStyleFuturistic = """
QProgressBar {
    border: 3px solid #333;
    border-radius: 10px;
    background-color: #444;
    height: 25px;
    text-align: center;
    color: #EEE;
}

QProgressBar::chunk {
    border-radius: 8px;
    background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, 
                      stop:0 rgba(255, 0, 0, 0), 
                      stop:0.2 rgba(255, 69, 0, 1), 
                      stop:0.5 rgba(255, 0, 0, 0.5),
                      stop:0.8 rgba(255, 69, 0, 1), 
                      stop:1 rgba(255, 0, 0, 0));
    margin: 1px;
    background-repeat: no-repeat;
    background-position: left;
}

QProgressBar {
    background-color: #222;
    color: #EEE;
    font-weight: bold;
}

QProgressBar::chunk {
    background-color: qlineargradient(
        x1: 0, y1: 0.5, x2: 1, y2: 0.5, 
        stop: 0 #F00, stop: 0.5 #F00, stop: 1 #F00);
}
"""
