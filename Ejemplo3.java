import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;

public class Ejemplo3{
	public static void main(String[] args){
		List<String> lista=Arrays.asList("Lunes", "Martes", "Miercoles", "Jueves", "Viernes");
		Collection<String> lista1= new ArrayList<> (lista);
		System.out.println();
	}
}