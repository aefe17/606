# 606 Fesisa

This is a Python Tkinter application for managing and saving financial data according to DGII F 606 regulations.

## Requirements

- Python 3.x
- Tkinter (usually included in Python installations)

## Usage

1. Clone the repository:
2. Navigate to the project directory:
3. Run the application:
4. Enter the required information and click on "Guardar Título" to firstly store the header values, then click on "Añadir nueva linea" to save all the other values to a file.

## Functionality

- **update_date**: This function updates the date entry widget and the comprobante pago entry widget with the previous month's date.
- **update_entry_RNC_Type_value**: This function updates the entry_RNC_Type widget based on the length of the RNC value entered.
- **save_values**: This function saves the entered values to a file named `DGII_F_606_{rnc_companina}_{periodo}.txt`.
- **append_values**: This function appends a new line of data to the existing file.

## Contributing

Contributions are welcome! Please feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
