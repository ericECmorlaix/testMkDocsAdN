#import ...

def define_env(env):
  "Hook function"

  @env.macro
  def hello() :
      return "_Demat d'an holl_"