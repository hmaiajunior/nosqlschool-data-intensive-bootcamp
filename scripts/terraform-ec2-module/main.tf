# Aqui chamaremos o módulo que criará nossa instância EC2.

module "ec2_module" {
  source         = "./modules/ec2"
  instance_name  = "my-db-server"
  instance_type  = "t2.micro"
  key_pair_name  = "key-pair-srv-bootcamp-1"  # Substitua com seu key pair existente na AWS
  vpc_id         = null                  # Se quiser criar em uma VPC específica, informe-a. Caso contrário, usa VPC default.
  subnet_id      = null                  # Se quiser especificar a subnet. Caso contrário, usa subnet default.
}
