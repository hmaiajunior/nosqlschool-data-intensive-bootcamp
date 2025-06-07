# Esse arquivo expõe a informação de IP público da instância e o ID do security group criado, para que possamos utilizá-las em outros lugares (caso necessário).

output "instance_public_ip" {
  description = "Endereço IP publico da instancia"
  value       = aws_instance.this.public_ip
}

output "security_group_id" {
  description = "ID do security group criado"
  value       = aws_security_group.allow_all_traffic.id
}
