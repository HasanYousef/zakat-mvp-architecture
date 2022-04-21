from diagrams import Cluster, Edge, Diagram
from diagrams.custom import Custom

from diagrams.digitalocean.compute import Droplet
from diagrams.digitalocean.database import DbaasPrimary
from diagrams.saas.identity import Auth0
from diagrams.programming.language import Nodejs
from diagrams.programming.framework import React
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.network import Nginx
from diagrams.generic.device import Mobile
from diagrams.aws.storage import S3

with Diagram("zakat.ibarakah MVP architecture (low level)", show=False):
    client = Mobile("Client")

    with Cluster("Client server"):
        graphQLClient = Custom("GraphQL (Apollo Client)", "graphQL.png")
        nextjs = Custom("for SSR", "nextjs.png")
        react = React("React.js")

    with Cluster("Backend server"):
        Droplet("DigitalOcean Droplet (Ubunto Linux machine)")
        with Cluster("Secure web serving"):
            nginx = Nginx("NGINX")
            letsEncrypt = Custom("SSL", "letsEncrypt.png")
        with Cluster("Business logic"):
            graphQLServer = Custom("GraphQL (Apollo Server)", "graphQL.png")
            nodejs = Nodejs("Node.js")
            sequelize = Custom("Sequelize.js ORM", "sequelize.png")
    
    with Cluster("Database"):
        postgres = PostgreSQL("PostgreSQL")
        DbaasPrimary("DigitalOcean primary DB")

    s3 = S3("AWS S3 bucket")


    auth = Custom("Google authentication", "googleAuth.png")

    client >> nextjs >> graphQLClient >> nginx >> graphQLServer >> nodejs >> sequelize >> postgres

    nodejs >> s3

    nodejs >> Edge() << auth
    client >> auth