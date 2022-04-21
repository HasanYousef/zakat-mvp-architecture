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

with Diagram("zakat.ibarakah MVP architecture (level 3)", show=False):
    client = Mobile("Client")
    auth = Custom("Google authentication", "googleAuth.png")
    s3 = S3("AWS S3 bucket (file storage)")

    with Cluster("Client server (Vercel)"):
        nextjs = Custom("Next.js (React.js)", "nextjs.png")

    with Cluster("Backend (DigitalOcean Droplet)"):
        nodejs = Nodejs("Node.js")
    
    with Cluster("Database (DigitalOcean DB)"):
        postgres = PostgreSQL("PostgreSQL")

    nodejs >> s3

    nodejs >> Edge() << auth
    client >> auth

    client >> nextjs >> nodejs >> postgres