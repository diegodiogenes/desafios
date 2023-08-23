NAME=reddit-scrapper
; := ;

.check-image-exists:
ifeq ($(shell docker images -q ${NAME}),)
	@docker build -t ${NAME} .
endif

.check-container-running:
ifeq ($(shell docker ps | grep ${NAME}),)
	@docker run --name ${NAME} --rm -d -it -v $(shell pwd):/app -p 8080:8080 ${NAME}
endif

run: .check-image-exists .check-container-running
	@docker exec -it ${NAME} bash

help: .check-image-exists .check-container-running
	@docker exec -it ${NAME} python main.py --help
