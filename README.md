# xmltotree
## How it works:
### Start service:

- #### Download sources:

  `git clone https://github.com/slava-mokrousov/xmltotree`

- #### Change current directory to project directory:

  `cd xmltotree`

- #### Build docker image:

  `./gradlew buildImage`

- #### Start service: 

  `docker run --rm -p 80:80 xml2tree`

### Send file:

    curl -d @test.xml http://localhost/post