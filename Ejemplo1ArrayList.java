import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;

public class Ejemplo1ArrayList {
	public static void main(String[] args) {
		//Inicializar la lista con Arrays.asList
		List<String> lista = ArraysList("Lunes", "Martes", "Miercoles", "Jueves", "Viernes");
		
		//Crear una nueva lista a partir de la lista inicial usando Collection
		Collection<String> lista1 = new ArrayList<>(lista);
		
		//Imprimir la lista inicial
		System.out.println("Lista inicial 1: " + lista1);
		
		//Crear una lista de caracteres
		ArrayList<Character> lista2 = new ArrayList<>();
		lista2.add('a');
		lista2.add('b');
		lista2.add('c');
		lista2.add('d');
		lista2.add('e');
		System.out.println("Lista 2: " + lista2);
		
		//Modificar el tercer elemnto de lista2
		lista2.set(2, 'x');
		System.out.println("Lista 2 despues de set: " + lista2);
		
		//Eliminar el tercer elemento de lista2
		lista2.remove(2)
		System.out.println("Lista 2 despues de remove: " + lista2);
		
		//Volver a agregar el caracter 'c' en la tercera posicion
		lista.add(2, 'c');
		System.out.println("Lista 2 despues de agregar 'c': " + lista2);
	}
}