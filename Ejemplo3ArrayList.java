import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Ejemplo3ArrayList {
	public static void main(String[] args) {
		
		//Inicializar un ArrayList de enteros 
		ArrayList<Integer> lista = new ArrayList<>();
		
		//Añadir varios elementos a la lista usando Arrays.asList
		lista.addAll(Arrays.asList(1,2,3,4,5,1,2,3,4,5));
		
		//Imprimir la lista inicial
		System.out.println("Lista Inicial: \t\t\t " + lista);
		
		//Convertir la lista en un arreglo de objetos
		Object[] listaArray = lista.toArray();
		System.out.println("Copia en Array: \t\t\t " + Arrays.toString(listaArray));
		
		//Crear una sublista desde la posicion 7 a la 9
		List<Integer> subLista = lista.subList(7,9);
		//Eliminar los elementos de la sublista (3 y 4)
		subLista.clear();
		System.out.println("Lista modificada: \t\t " + lista);
		
		//Eliminar la primera aparicion del numero 1
		lista.remove((Object) 1);
		System.out.println("Lista sin el primer '1': \t " + lista);
		
		//Comprobar si queda otro '1' en la lista
		System.out.println("Hay otro '1': \t\t " + lista.contains(1));
		
		//Imprimir y vaciar la lista
		System.out.println("Elementos de la lista: ");
		while (!lista.isEmpty()) {
			Integer dato = lista.get(0);
			System.out.print(dato + "");
			lista.remove(0);
		}
		System.out.println("\nLista vacia. Operacion completa.");
	}
}