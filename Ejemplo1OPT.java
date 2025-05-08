import java.util.List;
import java.util.ListIterator;

public class Ejemplo1{
	public static void main(String[] args){
		// Inicializar la lista con Arrays.aslist
		List<String> lista=Array.asList("Lunes","Martes","Miercoles","Jueves","Viernes");
		
		//Imprimir la lista inicial
		System.out.println("Lista Inicial"+lista);
		
		//Imprimir el primer elemento se lo indico por posicion de la lista
		System.out.println("Primer  elemento"+lista.get(0));
		
		//Recorrer la lista con un bucle foreach
		System.out.println("Recorrer con Foreach: ");
		for (String dato:lista){
		System.out.println(dato);
		}
		
		//Recorrer la lista con un iterador
		System.out.println("\n Recorrer con bucle iterador");
		Iterator<String> dato1 = lista.iterator();
		//Mientras haya siguientes elementos(hasNext) a recorrer
		while(iterador.hasNext()){
			//next obtiene el elemento de la lista
			System.out.println(iterador.next());
		}
		//Recorrer la lista con un ListIterator en orden inverso
		System.out.println("\n Recorrer la lista con ListIterator en orden inverso: ");
		//Se situa en la ultima posicion
		ListIterator<String> li=lista.listIterator(lista.size());
		while( li.hasPrevious()){
			//previous me permite obtener el elemento
			System.out.print(li.previous()+"");
		}
		
	}
}