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

with Diagram("zakat.ibarakah MVP architecture (medium level)", show=False):
    client = Mobile("Client")
    auth = Custom("Google authentication", "googleAuth.png")

    with Cluster("Client server"):
        nextjs = Custom("for SSR", "nextjs.png")
        react = React("React.js")

    with Cluster("Backend server"):
        nodejs = Nodejs("Node.js")
        Droplet("DigitalOcean Droplet")
    
    with Cluster("Database"):
        postgres = PostgreSQL("PostgreSQL")
        DbaasPrimary("DigitalOcean primary DB")

    s3 = S3("AWS S3 bucket")

    nodejs >> Edge() << auth
    client >> auth

    client >> nextjs >> nodejs >> postgres

    nodejs >> s3