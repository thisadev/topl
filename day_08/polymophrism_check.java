class Box<T> {
    private T content;

    public Box(T content) {
        this.content = content;
    }

    public T getContent() {
        return content;
    }

    public void showContentType() {
         if (content != null) {
            System.out.println("Box actually contains an object of type: " + content.getClass().getName());
         } else {
            System.out.println("Box content is null.");
         }
    }
}

public class SimpleGenericDemo {

    public static void main(String[] args) {

        Box<Integer> integerBox = new Box<Integer>(123);
        Box<String> stringBox = new Box<String>("Hello Generics!");
        Box<Double> doubleBox = new Box<>(3.14159);

        System.out.println("--- Integer Box ---");
        integerBox.showContentType();
        Integer intValue = integerBox.getContent();
        System.out.println("Content value: " + intValue);

        System.out.println("\n--- String Box ---");
        stringBox.showContentType();
        String strValue = stringBox.getContent();
        System.out.println("Content value: " + strValue);

        System.out.println("\n--- Double Box ---");
        doubleBox.showContentType();
        Double doubleValue = doubleBox.getContent();
        System.out.println("Content value: " + doubleValue);

    }
}
