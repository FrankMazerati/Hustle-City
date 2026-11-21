#include "HustleCityGameMode.h"
#include "HCPlayerCharacter.h"

AHustleCityGameMode::AHustleCityGameMode()
{
    DefaultPawnClass = AHCPlayerCharacter::StaticClass();
}
