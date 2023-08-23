NAME=crawlers-challenge

.check-image-exists:
ifeq ($(shell docker images -q ${NAME}),)
	@docker build -t ${NAME} . --no-cache
endif

.check-container-running:
ifeq ($(shell docker ps | grep ${NAME}),)
	@docker run --name ${NAME} -d ${NAME}
endif

run: .check-image-exists .check-container-running
	@docker exec -it ${NAME} bash

help: .check-image-exists .check-container-running
	@docker exec -it ${NAME} python main.py --help
