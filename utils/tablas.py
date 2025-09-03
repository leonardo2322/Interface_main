from flet import Column, Row, MainAxisAlignment, CrossAxisAlignment, DataTable, DataColumn, DataRow, DataCell, Text, IconButton, Icons, Colors, Margin, border,BorderSide, TextField
from config.tipografia import texto
from utils.dialogo import dlg_callback
from typing import List, Tuple

class DataTableManager(Column):
    def __init__(self, main,dlg,page,listar= None,*args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.main = main
        self.listar = listar
        self.show_dlg = dlg
        self.page = page
        self.head_table = None
        self.margin = Margin(left=10, top=10, right=10, bottom=20)
        self._tables = {}

    def create_data_table(self, head_table:str, table_items:list, data=[], services:dict = {}):
        """
        Genera una tabla con los datos proporcionados.
        
        Parámetros:
            head_table (str): Nombre de la tabla.
            table_items (list): Lista de encabezados.
            data (list, opcional): Lista de tuplas con los datos.

        Retorna:
            ft.DataTable: Una instancia de DataTable con los datos cargados.
        """
        self.head_table = head_table
        # Mapeo de clases según el tipo de tabla debe estar definida de esta manera y pasada por parametro

        servicios = {
            key: val for key, val in services.items() 
        }
        self.servicio = servicios.get(head_table, None)
        print(self.servicio,"self.servicio en crear tabla ------------")
        table = DataTable(
            expand=True,
            border=border.all(0, "#D1D5DB"),
            heading_row_color=Colors.BLUE_100,
            data_row_color=Colors.WHITE10,
            heading_row_height=45,
            divider_thickness=0.5,
            vertical_lines=BorderSide(0.7, "black"),
            horizontal_lines=BorderSide(0.7, "black"),
            columns=[
                DataColumn(
                    label=Text(
                        "Fecha " if item == "fecha" else item,
                        color=Colors.BLACK
                    )
                ) for item in table_items
            ] + [
                DataColumn(label=Text("Opciones", color=Colors.BLACK))
            ]
        )

        # Si hay datos, crea las filas
        if data:
            table.rows = [
            DataRow(
                cells=[
                    DataCell(
                        Text(f"{cell:.4f}" if isinstance(cell, float) and i in [5, 8] else cell,
                             size=12, color=Colors.WHITE)
                    ) for i, cell in enumerate(row)
                ] + [
                    DataCell(Row(controls=[
                        IconButton(icon="create", icon_color="blue",data={"row":row,"row_id":row[0],"nombre":row[2]}, on_click=lambda e, r=row: self.edit_row(e, self.servicio)),
                        IconButton(icon=Icons.DELETE, icon_color="red", data={"row":row,"row_id":row[0],"nombre":row[2]if self.head_table =="Pacientes" else row[1]}, on_click=lambda e:self.permiso_eliminar(e)),
                    ], spacing=12))
                ]
            ) for row in data
        ]
        self._tables[head_table] = (table, table_items)
        return table

    
    def refresh_data(self, new_data: List[Tuple]):
        return [
            DataRow(
                cells=[
                    DataCell(
                        Text(f"{cell:.4f}" if isinstance(cell, float) and i in [5, 8] else cell,
                             size=12, color=Colors.WHITE)
                    ) for i, cell in enumerate(row)
                ] + [
                    DataCell(Row(controls=[
                        IconButton(icon="create", icon_color="blue",data={"row":row,"row_id":row[0],"nombre":row[2]}, on_click=lambda e, r=row: self.edit_row(e, self.servicio)),
                        IconButton(icon=Icons.DELETE, icon_color="red", data={"row":row,"row_id":row[0],"nombre":row[2]if self.head_table =="Pacientes" else row[1]}, on_click=lambda e:self.permiso_eliminar(e)),
                    ], spacing=12))
                ]
            ) for row in new_data
        ]
    def edit_row(self,e):
        """Método para editar una fila"""
        # Aquí podrías abrir un modal o actualizar datos en la base
        data = e.control.data
        row = data.get("row")
        row_id = data.get("row_id")
        nombre = data.get("nombre")
        sexo = row[4]
        edad = row[3]
        resultado = TextField(label="Resultado paciente", hint_text="Introduzca El resultado del paciente")

        async def on_guardar_resultado(ev):
            async def wrapper(ev):
                await self.actualizar_paciente(ev, row_id, resultado.value, self.servicio)
            await wrapper(ev)
            self.main.update()
        datos = Column(
            controls=[
               Row(
                   controls=[
                        texto("ID:"),
                texto(row_id),
                texto("Nombre del Paciente:"),
                texto(nombre),
               
                   ],
                   alignment=MainAxisAlignment.CENTER
               ),
               Row(
                   controls=[
                        texto("Sexo:"),
                texto("Masculino") if sexo == "M" else texto("Femenino"),
                texto("Edad: "),
                texto(edad)
                   ],
                   alignment=MainAxisAlignment.CENTER
               ),

                Row(
                    controls=[
                        resultado,

                    ],
                    alignment=MainAxisAlignment.CENTER
                    )
            ],
            spacing=10,
            alignment=MainAxisAlignment.CENTER,horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        dlg_callback(self,e=e,page=self.page,content=datos,title="Formulario para cambio del resultado del paciente", icon=Icons.NOTE_ADD,color_icon="blue", action_def=on_guardar_resultado,win_height=250)
        
        
    async def actualizar_paciente(self,e,id,resultado):
        instancia = self.servicio
        # result = await instancia.actualizar_paciente_resultado(id,resultado)
        # if result:
        #     dlg_callback(self,e=e,page=self.page,content=Text("El usuario ha sido actualizado exitosamente"),title=f"Usuario actualizado correctamente",icon=Icons.CHECK,color_icon="green",win_height=200,icon_btn=Icons.CHECK)
        # else:
        #     dlg_callback(self,e=e,page=self.page,content=Text("ha ocurrido un error"),title=f"ha ocurrido un error",icon=Icons.CHECK,color_icon="red",win_height=200,icon_btn=Icons.WARNING)
        # await self.listar(e)


    def permiso_eliminar(self,e):
        data = e.control.data
        row_id = data.get("row_id")
        nombre = data.get("nombre")
        dlg_callback(self,e=e,page=self.page,content=Text("Presiona aceptar para eliminar si estas seguro",color=Colors.AMBER),title=f"Estas seguro de querer Eliminar a {nombre}",icon=Icons.WARNING,color_icon="red",action_def=lambda e:self.delete_row(e,row_id,nombre),win_height=200,icon_btn=Icons.DELETE)
        
    def delete_row(self,e, row_id,nombre):
        """Método para eliminar una fila"""
        try:
            resultado = self.servicio.delete(id=row_id)
            # self.listar(e)
            if 'success' in resultado:
                new_data = self.listar()
                tabla = self._tables.get(self.head_table)
                if tabla:
                    tabla[0].rows = self.refresh_data(new_data)
                # self.refresh_data(self.head_table,new_data, self.servicio)
                return dlg_callback(self,e=e,page=self.page,content=Text("El usuario ha sido eliminado exitosamente",color=Colors.GREEN),title=f"eliminaste a {nombre}",icon=Icons.CHECK,color_icon=Colors.GREEN,win_height=140,icon_btn=Icons.CHECK)
        except Exception as ex:
            return dlg_callback(self,e=e,page=self.page,content=Text(f"El error es: {ex}",color=Colors.RED),title=f"Error de ejecucion",icon=Icons.CHECK,color_icon="red",win_height=140,icon_btn=Icons.WARNING)

