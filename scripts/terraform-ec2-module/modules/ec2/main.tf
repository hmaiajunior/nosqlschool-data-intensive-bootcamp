# Aqui, criamos o Security Group que permite todo o tráfego inbound e outbound e, em seguida, a instância EC2 associada.


# Security Group:

# ingress e egress estão configurados com -1 para protocol, indicando todos os protocolos, e 0 como as portas para permitir tráfego irrestrito de entrada e saída.

# cidr_blocks = ["0.0.0.0/0"] e ipv6_cidr_blocks = ["::/0"] permitem acesso de qualquer IP IPv4 e IPv6.

# Atenção: Permitir todo o tráfego inbound e outbound é extremamente permissivo e, em ambientes de produção, deve-se restringir o tráfego conforme necessidades específicas.



# aws_instance:

# ami = data.aws_ami.amazon_linux.id utiliza um data source para buscar a AMI mais recente do Amazon Linux 2.

# vpc_security_group_ids aplica o Security Group criado à instância.

# key_name recebe um key pair existente na AWS para acesso SSH.

# subnet_id pode ser deixado em branco se quisermos que a AWS selecione a subnet default; caso queira especificar, basta passar o ID da subnet via variável.


resource "aws_security_group" "allow_all_traffic" {
  name        = "${var.instance_name}-sg"
  description = "Security group que permite todo trafego"
  
  vpc_id      = var.vpc_id

  # Regras de Inbound
  ingress {
    description      = "Permitir todo trafego inbound"
    from_port        = 0
    to_port          = 0
    protocol         = "-1"   # -1 significa todos os protocolos
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  # Regras de Outbound
  egress {
    description      = "Permitir todo trafego outbound"
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  # Tags opcionais
  tags = {
    Name = "${var.instance_name}-sg"
  }
}

resource "aws_instance" "this" {
  #count = 1
  
  ami                         = data.aws_ami.amazon_linux.id
  instance_type               = var.instance_type
  key_name                    = var.key_pair_name
  vpc_security_group_ids      = [aws_security_group.allow_all_traffic.id]

  # Se vpc_id for nulo, a instância será criada na VPC/Subnet default.
  # Caso contrário, utilize var.subnet_id também.
  subnet_id                   = var.subnet_id

  tags = {
    Name = var.instance_name
  }
}

# Buscar a última versão da AMI do Amazon Linux (exemplo)
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm*"]
  }
}
