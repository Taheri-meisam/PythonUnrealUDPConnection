#pragma once

#include "Serialization/Archive.h"
#include "UDPData.h"
#include "Networking.h"
#include "GameFramework/Actor.h"
#include "UDPSender.generated.h"

UCLASS()
class UDPCOMMUNICATION_API AUDPSender : public AActor
{
	GENERATED_UCLASS_BODY()

public:
	TSharedPtr<FInternetAddr> RemoteAddr;
	FSocket* SenderSocket;

	UFUNCTION(BlueprintCallable, Category = "UDPCommunication")
		bool StartUDPSender(const FString& SocketName, const FString& TheIP, const int32 ThePort);

	UFUNCTION(BlueprintCallable, Category = "UDPCommunication")
		bool UDPSendArray(FUDPData data);

public:

	virtual void EndPlay(const EEndPlayReason::Type EndPlayReason) override;

}
;