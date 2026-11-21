#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "HCPlayerCharacter.generated.h"

class USpringArmComponent;
class UCameraComponent;

/**
 * First playable Hustle City player pawn.
 * Input is intentionally kept simple for the first desktop vertical slice.
 */
UCLASS()
class HUSTLECITY_API AHCPlayerCharacter : public ACharacter
{
    GENERATED_BODY()

public:
    AHCPlayerCharacter();

protected:
    virtual void BeginPlay() override;
    virtual void SetupPlayerInputComponent(UInputComponent* PlayerInputComponent) override;

private:
    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category="Camera", meta=(AllowPrivateAccess="true"))
    TObjectPtr<USpringArmComponent> CameraBoom;

    UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category="Camera", meta=(AllowPrivateAccess="true"))
    TObjectPtr<UCameraComponent> FollowCamera;

    void MoveForward(float Value);
    void MoveRight(float Value);
    void Turn(float Value);
    void LookUp(float Value);
};
