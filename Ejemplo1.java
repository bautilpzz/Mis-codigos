import java.util.List;
import java.util.ListIterator;

public class Ejemplo1{
	public static void main(String[] args){
		//Declaracion de la lista
		List<String> lista=Array.asList("Lunes","Martes","Miercoles","Jueves","Viernes");
		System.out.println("Lista Inicial"+lista);
		System.out.println("Primer  elemento"+lista.get(0));
		
		System.out.println("Recorrer con Foreach");
		
		for (String dato:lista){
		System.out.println(dato+" ");
		}
		
		System.out.println("\n Recorrer con bucle iterador");
		Iterator<String> dato1 = lista.iterator();
		while(dato1.hasNext()){
			System.out.println(dato1.next() + "");
		}
		System.out.println("\n Recorrer iterator extendido");
		ListIterator<String> li=lista.listIterator(lista.size());
		while( li.hasPrevious()){
			System.out.print(li.previous()+"");
		}
		
	}
}