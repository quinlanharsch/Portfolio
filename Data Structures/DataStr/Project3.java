public class Project3 {
    /**
     * How would you do this with generics? I meant to ask you friday, but I forgot
     * cuz' of the guest speaker. Thanks, hope you enjoy :)
     */
    public static class Triangle {
        // Internal Variables
        private double side1;
        private double side2;
        private double side3;

        // 1337 constructor
        Triangle(double a, double b, double c) {
            side1 = a;
            side2 = b;
            side3 = c;
        }

        // N00B constructor
        Triangle() {
            side1 = 1.0;
            side2 = 1.0;
            side3 = 1.0;
        }

        //Internal commands:
        double findPerimeter() {
            return side1 + side2 + side3;
        }

        double findArea() { // uses the suggested method
            double p = findPerimeter() / 2;
            return Math.sqrt(p * (p - side1) * (p - side2) * (p - side3));
        }

        boolean isEquilateral() {
            return side1 == side2 && side2 == side3;
        }

        // don't need an if then, because the () part of an "if" is already a boolean expression
        boolean isIsosceles() {
            return side1 == side2 || side2 == side3 || side3 == side1;
        }

        // equilateral triangles are also technically isosceles
        boolean isScalene() {
            return !isIsosceles();
        }

        boolean isRight() {
            return  (side1 * side1) + (side2 * side2) == (side3 * side3) ||
                    (side2 * side2) + (side3 * side3) == (side1 * side1) ||
                    (side3 * side3) + (side1 * side1) == (side2 * side2);
        }
    }

    public static void main(String[] args) {
        // Make a triangle
        Triangle t = new Triangle(3, 3, 3);

        // Get the area
        System.out.println("Triangle's area is: " + t.findArea());

        // Get the perimeter
        System.out.println("Triangle's perimeter is: " + t.findPerimeter());

        String isEquilateral = "No";
        String isIsosceles = "No";
        String isScalene = "No";
        String isRight = "No";

        // Check each property and update the string as needed

        if (t.isEquilateral()) {
            isEquilateral = "Yes";
        }

        if (t.isIsosceles()) {
            isIsosceles = "Yes";
        }

        if (t.isScalene()) {
            isScalene = "Yes";
        }

        if (t.isRight()) {
            isRight = "Yes";
        }

        System.out.println("Is the triangle an equilateral triangle? " + isEquilateral);
        System.out.println("Is the triangle an isosceles triangle? " + isIsosceles);
        System.out.println("Is the triangle a scalene triangle? " + isScalene);
        System.out.println("Is the triangle a right triangle? " + isRight);
    }
}
