variable "instance_name" {
  type        = string
  description = "Nome da instancia EC2"
}

variable "instance_type" {
  type        = string
  description = "Tipo da instancia EC2"
  default     = "t2.micro"
}

variable "key_pair_name" {
  type        = string
  description = "Nome do key pair que sera associado a instancia"
}

variable "vpc_id" {
  type        = string
  description = "ID da VPC onde a instancia sera criada"
  default     = null
}

variable "subnet_id" {
  type        = string
  description = "ID da Subnet onde a instancia sera criada"
  default     = null
}
