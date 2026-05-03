class UserModel {
  final String uid;
  final String email;
  final String name;
  final String role; // 'user' or 'trainer'
  final int age;
  final double weight;
  final String goal;

  UserModel({
    required this.uid,
    required this.email,
    required this.name,
    this.role = 'user',
    this.age = 0,
    this.weight = 0.0,
    this.goal = '',
  });

  Map<String, dynamic> toMap() {
    return {
      'uid': uid,
      'email': email,
      'name': name,
      'role': role,
      'age': age,
      'weight': weight,
      'goal': goal,
    };
  }
}