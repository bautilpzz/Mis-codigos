import java.util.List;
import java.util.Arrays;
public class Ejemplo2{
	public static void main(String[] args){
		
		List<integer> lista= Arrays.asList(1,2,3,4,5,1,2);
		
		//Imprimir la lista inicial
		System.out.println("Lista Inicial"+ lista);
		
		//Obtener el primer indice de '1'
		System.out.println("El elemento 1 es: "+lista.indexOf(1));
		
		//Obtener el ultimo indice de '1'
		System.out.println("El ultimo '1' esta en: " + lista.lastIndexOf(1);
		
		//Crear una sublista de la lista original
		List<Integer> sublista=lista.subList(2,5);
		
		System.out.println("Sublista:[3-5]"+sublista);
	}
}
