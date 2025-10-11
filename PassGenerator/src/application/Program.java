private static String generatePassword(String chars, int length) {
    Random rand = new Random();
    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < length; i++) {
        int index = rand.nextInt(chars.length());
        sb.append(chars.charAt(index));
    }

    return sb.toString();
}


void main() {
    String lowerLetters = "abcdefghijklmnopqrstuvwxyz";
    String upperLetters = lowerLetters.toUpperCase();
    String numbers = "0123456789";
    String symbols = "[]{};/\\\\~^´`'\\\"?:<>,.!@#$%¨&*()-_=+ç";

}
