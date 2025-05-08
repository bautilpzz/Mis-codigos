import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;

public class Ejemplo2ArrayList {
	public static void main(String[] args) {
		
		ArrayList<Integer> lista = new ArrayList <>();
		
		lista.addAll(Array.asList(1,2,3,4,5,1,2,3,4,5));
		
		//Imprimir la lista inicial
		System.out.println("Lista inicial: \t\t\t " + lista);
		
		Object[] listaArray = new Integer[lista.size()];
		listaArray=lista.toArray();
		
		System.out.println("Lista 2: "+ lista2);
		
		//Modificar e tercer elemento de lista2
		lista2.set(2, 'x');
		System.out.println("Lista 2 despues de set: " + lista2);
		
		//Eliminar el tercer elemento de lista2
		lista2.remove(2);
		System.out.println("Lista 2 despues de remove: " + lista2);
		
		//Volver a agregar el caracter 'c' en la tercera posicion
		lista2.add(2, 'c');
		System.out.println("Lista 2 despues de agregar 'c': " + lista2);
	}
}
		